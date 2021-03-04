import {Entity, PrimaryGeneratedColumn, Column} from "typeorm";

@Entity()
export class User {

    @PrimaryGeneratedColumn()
    id: number = 0;

    @Column()
    naam: string = "unset";

    @Column()
    paswoord: string = "unset";

    @Column()
    nummerplaat: string = "unset";

}
