import {Entity, PrimaryGeneratedColumn, Column} from "typeorm";

@Entity()
export class user {

    @PrimaryGeneratedColumn()
    ID: number;

    @Column()
    naam: string;

    @Column()
    paswoord: string;

    @Column()
    nummerplaat: string;

}
