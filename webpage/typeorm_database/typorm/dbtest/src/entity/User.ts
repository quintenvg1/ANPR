import {Entity, PrimaryGeneratedColumn, Column} from "typeorm";

@Entity()
export class User {

    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    naam: string;

    @Column()
    paswoord: string;

    @Column()
    nummerplaat: string;

}
